import grpc
from concurrent import futures
import shopping_platform_pb2
import shopping_platform_pb2_grpc


class MarketServicer(shopping_platform_pb2_grpc.SellerServiceServicer,
                     shopping_platform_pb2_grpc.BuyerServiceServicer):

    def __init__(self):
        self.sellers = {}  # Stores seller information
        self.items = {}    # Stores item information
        self.registered_uuid=set()
        self.registered_uuid.add("abc")
        self.registered_seller_addresses = set()  # Initialize a set to store registered seller addresses
        self.item_ratings = {}  # Dictionary to store item ratings
        self.buyer_wishlist = {}  # Dictionary to store buyer wishlists

    # Other methods...
    def Login(self, request, context):
        print(f"Login request from {context.peer()}, uuid={request.uuid}")
        for i in self.registered_uuid:
            print(i)
        if(request.uuid not in self.registered_uuid):
            return shopping_platform_pb2.CheckSellerResponse(status="FAIL")
        else:
            return shopping_platform_pb2.CheckSellerResponse(status="SUCCESS")

    def DisplayItems(self, request, context):
        print(f"Display Items request from {context.peer()}, uuid={request.seller_uuid}")

        matching_items = []
        for item in self.items.values():
            if item["seller_uuid"] == request.seller_uuid:
                matching_items.append(item)

        return shopping_platform_pb2.DisplayItemsResponse(items=matching_items)



    
    def RegisterSeller(self, request, context):
        # Print the seller join request message
        print(f"Seller join request from {context.peer()}, uuid = {request.uuid}")

        # Check if the seller's address is already registered
        if request.address in self.registered_seller_addresses:
            # If the address is already registered, send a FAILED response
            return shopping_platform_pb2.SellerResponse(status="FAIL")
        else:
            # If the address is not registered, accept the seller and send a SUCCESS response
            self.registered_seller_addresses.add(request.address)
            self.registered_uuid.add(request.uuid)
            return shopping_platform_pb2.SellerResponse(status="SUCCESS")


    def SellItem(self, request, context):
        # Generate unique item ID
        item_id = len(self.items) + 1
        print(f"Sell Item request from {context.peer()}, uuid={request.seller_uuid}")
        # Store item information
        self.items[item_id] = {
            'id':item_id,
            'name': request.name,
            'category': request.category,
            'quantity': request.quantity,
            'description': request.description,
            'price': request.price,
            'seller_address': request.seller_address,
            'seller_uuid': request.seller_uuid
        }
        # Return response
        #return shopping_platform_pb2.SellerResponse(status="Item listed for sale successfully.")
        # Return response with item ID
        return shopping_platform_pb2.SellerResponse(status="Item listed for sale successfully.", item_id=item_id)


    def SearchItem(self, request, context):
        print(f"Search request for Item name: {'<empty>' if not request.name else request.name}, Category: {request.category or 'ANY'}.")

        matched_items = []
        # Check if the request contains a specific item name and category
        if request.name and request.category:
            matched_items = [item for item in self.items.values() if
                             request.name.lower() in item['name'].lower() and
                             (request.category == 'ANY' or request.category == item['category'])]
        # Check if the request contains only a specific item name
        elif request.name:
            matched_items = [item for item in self.items.values() if
                             request.name.lower() in item['name'].lower()]
        # Check if the request contains only a specific item category
        elif request.category:
            matched_items = [item for item in self.items.values() if
                             request.category == 'ANY' or request.category == item['category']]
        # If neither name nor category is specified, return all items
        else:
            matched_items = list(self.items.values())

        # Create response with matched items
        items_response = []
        for id, item_details in enumerate(matched_items, start=1):
            item_id = id  # Using enumeration index as item ID for simplicity
            rating = self.item_ratings.get(item_id, 0)  # Get the rating from item_ratings dictionary
            item_response = shopping_platform_pb2.Item(
                name=item_details['name'],
                category=item_details['category'],
                description=item_details['description'],
                price=item_details['price'],
                quantity=item_details['quantity'],
                rating=rating,  # Assign retrieved rating to the item
                seller_address=item_details['seller_address']
            )
            items_response.append(item_response)

        return shopping_platform_pb2.SearchItemResponse(items=items_response)

    def UpdateItem(self, request, context):
        # Check if item exists and is owned by the seller
        print(f"Update Item {request.item_id} request from {context.peer()}")

        if request.item_id in self.items and \
                self.items[request.item_id]['seller_address'] == request.seller_address and \
                self.items[request.item_id]['seller_uuid'] == request.seller_uuid:
            # Update item information
            self.items[request.item_id]['price'] = request.price
            self.items[request.item_id]['quantity'] = request.quantity
            # Notify interested buyers
            # Return response
            return shopping_platform_pb2.SellerResponse(status="Item updated successfully.")
        else:
            return shopping_platform_pb2.SellerResponse(status="Item not found or you are not the owner.")

    def DeleteItem(self, request, context):
        # Check if item exists and is owned by the seller
        print(f"Delete Item {request.item_id} request from {context.peer()}")

        if request.item_id in self.items and \
                self.items[request.item_id]['seller_address'] == request.seller_address and \
                self.items[request.item_id]['seller_uuid'] == request.seller_uuid:
            # Remove item from the list
            del self.items[request.item_id]
            # Notify buyers
            # Return response
            return shopping_platform_pb2.SellerResponse(status="Item deleted successfully.")
        else:
            return shopping_platform_pb2.SellerResponse(status="Item not found or you are not the owner.")

    def AddToWishlist(self, request, context):
        # Get the item ID from the request
        item_id = request.item_id
        # Implement logic to add the item to the buyer's wishlist (you might have a data structure to store wishlists)
        # For example:
        buyer_wishlist = {}  # Assuming a dictionary to store wishlists where key is the buyer's ID and value is a list of item IDs
        buyer_id = request.buyer_id
        if buyer_id in buyer_wishlist:
            buyer_wishlist[buyer_id].append(item_id)
        else:
            buyer_wishlist[buyer_id] = [item_id]
            
        print(f"Wishlist request of item {item_id}, from {context.peer()}")

        # Return a response indicating the item has been added to the wishlist
        return shopping_platform_pb2.BuyerResponse(status="Item added to wishlist successfully.")

    def RateItem(self, request, context):
        print(f"{context.peer()} rated item {request.item_id} with {request.rating} stars.")
        # Get the item ID and rating from the request
        item_id = request.item_id
        
        self.items[item_id]["rating"]=request.rating
        

        # Return a response indicating the item has been rated
        return shopping_platform_pb2.BuyerResponse(status="Item rated successfully.")
    
    def NotifySeller(self, request, context):
        print("Notification received from buyer:", request.item)
        # You can add further logic here if needed
        return shopping_platform_pb2.Empty()  # Respond with an empty message

    
    def BuyItem(self, request, context):
        if request.item_id in self.items and self.items[request.item_id]['quantity'] >= request.quantity:
            # Update item quantity
            self.items[request.item_id]['quantity'] -= request.quantity
            # Log transaction
            print(f"Buy request {request.quantity} of item {request.item_id}, from {request.buyer_address}")
            
            # Notify seller about the purchase
            notification = shopping_platform_pb2.ItemNotification(item=self.items[request.item_id])
            seller_address = self.items[request.item_id]['seller_address']  # Retrieve seller's address
            with grpc.insecure_channel(seller_address) as channel:
                stub = shopping_platform_pb2_grpc.SellerServiceStub(channel)
                response = stub.NotifySeller(notification)
                print("Notification sent to seller:", response)

            # Return response
            return shopping_platform_pb2.BuyerResponse(status="Purchase successful.")
        else:
            return shopping_platform_pb2.BuyerResponse(status="Item not available or insufficient quantity.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    servicer = MarketServicer()
    shopping_platform_pb2_grpc.add_SellerServiceServicer_to_server(servicer, server)  # Add this line
    shopping_platform_pb2_grpc.add_BuyerServiceServicer_to_server(servicer, server)
    server.add_insecure_port('[::]:50001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
