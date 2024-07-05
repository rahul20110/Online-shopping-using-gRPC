# Online Shopping Platform using gRPC

## Overview
This project implements an online shopping platform using gRPC, consisting of three main components:

- **Market (Central Platform):** Connects buyers and sellers, handling accounts, items, transactions, and notifications.
- **Seller:** Manages item listings and transactions.
- **Buyer:** Searches for and purchases items.

Each component runs on separate Google Cloud VMs and communicates via gRPC.

## Functionality

### Seller to Market
- **RegisterSeller:** Registers a seller with the Market.
  - **Request:** Seller address (ip), UUID.
  - **Response:** SUCCESS or FAIL.
- **SellItem:** Posts a new item for sale.
  - **Request:** Item details (Name, Category, Quantity, Description, Seller Address, Price), UUID.
  - **Response:** SUCCESS, FAIL, or item ID.
- **UpdateItem:** Updates an item.
  - **Request:** Item ID, new Price, new Quantity, Seller Address, UUID.
  - **Response:** SUCCESS or FAIL.
- **DeleteItem:** Deletes an item.
  - **Request:** Item ID, Seller Address, UUID.
  - **Response:** SUCCESS or FAIL.
- **DisplaySellerItems:** Displays all items uploaded by the seller.
  - **Request:** Seller Address, UUID.
  - **Response:** List of items with details.

### Buyer to Market
- **SearchItem:** Searches for items.
  - **Request:** Item name, Item category.
  - **Response:** List of items with details.
- **BuyItem:** Purchases an item.
  - **Request:** Item ID, Quantity, Buyer Address.
  - **Response:** SUCCESS or FAIL.
- **AddToWishList:** Adds an item to the wishlist.
  - **Request:** Item ID, Buyer Address.
  - **Response:** SUCCESS or FAIL.
- **RateItem:** Rates an item.
  - **Request:** Item ID, Buyer Address, Rating (1-5).
  - **Response:** SUCCESS or FAIL.

### Market to Buyer/Seller
- **NotifyClient:** Sends notifications about updated item details.

## Protobuf Definitions
Separate proto definitions are used for each type of communication.

## Running the Platform
1. Deploy the Market on a Google Cloud VM.
2. Deploy Seller and Buyer Clients on separate VMs.
3. Set up gRPC servers for each component.
4. Use the provided gRPC client scripts to interact with the Market.

## Logging
Each communication logs received proto messages on both sides for debugging.

## Example Commands

### Seller Commands
- RegisterSeller: `python seller.py register --address 192.13.188.178:50051 --uuid 987a515c-a6e5-11ed-906b-76aef1e817c5`
- SellItem: `python seller.py sell --name iPhone --category ELECTRONICS --quantity 5 --description "This is iPhone 15" --price 500 --uuid 987a515c-a6e5-11ed-906b-76aef1e817c5`

### Buyer Commands
- SearchItem: `python buyer.py search --name "" --category ANY`
- BuyItem: `python buyer.py buy --id 3 --quantity 1 --address 120.13.188.178:50051`

## Conclusion
This gRPC-based platform manages buyers and sellers with a central market system, providing robust functionalities for a seamless shopping experience.
