import grpc
import shopping_platform_pb2
import shopping_platform_pb2_grpc
import uuid

class BuyerClient:
    def __init__(self, address, buyer_id):
        self.channel = grpc.insecure_channel(address)
        self.stub = shopping_platform_pb2_grpc.BuyerServiceStub(self.channel)
        self.buyer_id = buyer_id

        
    def search_item(self, search_request):
        response = self.stub.SearchItem(search_request)
        print("Buyer prints:")
        for item in response.items:
            print("–")
            print(f"Name: {item.name}, Category: {shopping_platform_pb2.Category.Name(item.category)}")
            print(f"Description: {item.description}, Price: {item.price}, Quantity: {item.quantity}")
            print(f"Rating: {item.rating} / 5, Seller: {item.seller_address}")
            print("–")


    def buy_item(self, buy_request):
        response = self.stub.BuyItem(buy_request)
        print("Item purchased:", response.status)

    def add_to_wishlist(self, wishlist_request):
        wishlist_request.buyer_id = self.buyer_id
        response = self.stub.AddToWishlist(wishlist_request)
        print("Item added to wishlist:", response.status)

    def rate_item(self, rate_request):
        response = self.stub.RateItem(rate_request)
        print("Item rated:", response.status)
        
    

    def notify(self, notification):
        response = self.stub.NotifyBuyer(notification)
        print("Notification received:", response)

if __name__ == '__main__':
    buyer_address = input("Enter your address (ip:port): ")
    buyer_id = str(uuid.uuid1())
    buyer_client = BuyerClient(buyer_address, buyer_id)

    while True:
        print("1. Search Item")
        print("2. Buy Item")
        print("3. Add to Wishlist")
        print("4. Rate Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            item_category = input("Enter item category (ELECTRONICS, FASHION, OTHERS): ")
            search_request = shopping_platform_pb2.SearchItemRequest(
                name=item_name,
                category=shopping_platform_pb2.Category.Value(item_category)
            )
            buyer_client.search_item(search_request)
        elif choice == '2':
            item_id = int(input("Enter item ID: "))
            quantity = int(input("Enter quantity: "))
            buyer_address = input("Enter your address (ip:port): ")
            buy_request = shopping_platform_pb2.BuyItemRequest(
                item_id=item_id,
                quantity=quantity,
                buyer_address=buyer_address
            )
            buyer_client.buy_item(buy_request)
        elif choice == '3':
            item_id = int(input("Enter item ID: "))
            wishlist_request = shopping_platform_pb2.AddToWishlistRequest(
                item_id=item_id,
                buyer_address=buyer_address
            )
            buyer_client.add_to_wishlist(wishlist_request)
        elif choice == '4':
            item_id = int(input("Enter item ID: "))
            rating = int(input("Enter your rating (1-5): "))
            rate_request = shopping_platform_pb2.RateItemRequest(
                item_id=item_id,
                buyer_address=buyer_address,
                rating=rating
            )
            buyer_client.rate_item(rate_request)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
