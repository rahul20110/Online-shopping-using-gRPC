import grpc
import shopping_platform_pb2
import shopping_platform_pb2_grpc
import uuid
class SellerClient:
    def __init__(self, address,uuid):
        self.channel = grpc.insecure_channel(address,options=(('grpc.enable_http_proxy', 0),))
        self.stub = shopping_platform_pb2_grpc.SellerServiceStub(self.channel)
        self.uuid = uuid
    def Login(self,seller_info):
        response=self.stub.Login(seller_info)
        # print(response)
        return response.status

    def register_seller(self, seller_info):
        response = self.stub.RegisterSeller(seller_info)

        return response.status

    def sell_item(self, item_info):
        response = self.stub.SellItem(item_info)
        print("Item listed for sale:", response.status)

    def update_item(self, update_info):
        response = self.stub.UpdateItem(update_info)
        print("Item updated successfully:", response.status)

    def delete_item(self, delete_info):
        response = self.stub.DeleteItem(delete_info)
        print("Item deleted successfully:", response.status)

    def display_items(self, display_info):
        response = self.stub.DisplayItems(display_info)
        print("Your items:")
        for item in response.items:
            print()
            print(f"ID: {item.id}")
            print(f"Name: {item.name}")
            print(f"Category: {shopping_platform_pb2.Category.Name(item.category)}")
            print(f"Price: {item.price}")
            print(f"Rating: {item.rating} / 5)")
            print(f"Quantity: {item.quantity}")
            print()

    def notify_seller(self, notification):
        response = self.stub.NotifySeller(notification)
        print("Notification received by seller:", response)


    def notify(self, notification):
        response = self.stub.Notify(notification)
        print("Notification received:", response)

if __name__ == '__main__':
    seller_address = "localhost:50001"
    flag=0
    

    while True:
        if(flag==1):
            break
        print("+"*20)
        print("1. New Seller")
        print("2. Already Registererd")
        print("3. Exit")
        print("+"*20)
        ch=input("Enter your choice: ")
        
        if(ch=='1'):
            seller_uuid = str(uuid.uuid1())
            seller_client = SellerClient(seller_address,seller_uuid)
            seller_info = shopping_platform_pb2.RegisterSellerRequest(address=seller_address, uuid=seller_uuid)
            re=seller_client.register_seller(seller_info)
            if(re=="FAIL"):
                print("FAIL: Only 1 seller allowed to register from IP address")
            else:
                print("Seller Registered Successfully: SUCCESS")
                print(f"Your uuid is: {seller_uuid}")
                print("Please keep the uuid safe with you :)")
        elif(ch=="2"):
            seller_uuid=input("Enter you uuid no. : ")
            seller_client = SellerClient(seller_address,seller_uuid)
            seller_info = shopping_platform_pb2.CheckSellerRequest(uuid=seller_uuid)
            res=seller_client.Login(seller_info)
            
            if(res=="FAIL"):
                print("Not Registered")
            else:
                
                print("+"*32)
                print("Welcome to the MarketPlace :)")
                
                while True:
                    print("-"*32)
                    print("1. Sell Item")
                    print("2. Update Item")
                    print("3. Delete Item")
                    print("4. Display Items")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        item_name = input("Enter item name: ")
                        item_category = input("Enter item category (ELECTRONICS, FASHION, OTHERS): ")
                        item_quantity = int(input("Enter item quantity: "))
                        item_description = input("Enter item description: ")
                        item_price = int(input("Enter item price: "))
                        print(seller_uuid)
                        try:
                            item_info = shopping_platform_pb2.SellItemRequest(
                                name=item_name,
                                category=shopping_platform_pb2.Category.Value(item_category),
                                quantity=item_quantity,
                                description=item_description,
                                price=item_price,
                                seller_address=seller_address,
                                seller_uuid=seller_uuid
                            )
                            seller_client.sell_item(item_info)
                        except Exception as e:
                            print(f"Error calling SellItem: {e}")
                    elif choice == '2':
                        item_id = int(input("Enter the ID of the item you want to update: "))
                        new_price = int(input("Enter the new price of the item: "))
                        new_quantity = int(input("Enter the new quantity of the item: "))
                        update_info = shopping_platform_pb2.UpdateItemRequest(
                            item_id=item_id,
                            seller_address=seller_address,
                            seller_uuid=seller_uuid,
                            price=new_price,
                            quantity=new_quantity
                        )
                        seller_client.update_item(update_info)
                    elif choice == '3':
                        #item_id = input("Enter the ID of the item you want to delete: ")
                        item_id = int(input("Enter the ID of the item you want to delete: "))

                        delete_info = shopping_platform_pb2.DeleteItemRequest(
                            item_id=item_id,
                            seller_address=seller_address,
                            seller_uuid=seller_uuid
                        )
                        seller_client.delete_item(delete_info)
                    elif choice == '4':
                        print(seller_uuid)
                        display_info = shopping_platform_pb2.DisplayItemsRequest(
                            seller_address=seller_address,
                            seller_uuid=seller_uuid
                        )
                        seller_client.display_items(display_info)
                    elif choice == '5':
                        flag=1
                        break
                    else:
                        print("Invalid choice")
        elif ch=="3":
            break
        else:
            print("Invalid Choice")
