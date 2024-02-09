"""Consumeing Api"""
import json
import httpx



async def fetchproduct(id):
    """Fethcing data"""
    try:
        if not id:
            url = "https://fakestoreapi.com/products"
        else:
            url = f"https://fakestoreapi.com/products/{id}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status() 
            parsed_data = json.loads(response.text)
            print(f"{parsed_data}")
    except httpx.HTTPError as e:
        print(f"Error fetching data: {e}")
        return None
    
async def delete_product(id):
    """Delete a product by ID"""
    try:
        url = f"https://fakestoreapi.com/products/{id}"
        async with httpx.AsyncClient() as client:
            response = await client.delete(url)
            response.raise_for_status()
            print(f"Product with ID {id} deleted successfully")
            return True
    except httpx.HTTPError as e:
        print(f"Error deleting product: {e}")
        return False

async def update_product(product_id, update_arg):
    data = {
        "title": update_arg,
        "price": 666,
        "description": "UPDATED",
        "image": "https://i.pravatar.cc",
        "category": "UPDATED"
    }
    try:
        url = f"https://fakestoreapi.com/products/{product_id}"
        async with httpx.AsyncClient() as client:
            response = await client.put(url, json=data)
            response.raise_for_status()
            updated_product = response.json()
            print(updated_product)
            return updated_product
    except httpx.HTTPError as e:
        print(f"Error updating product: {e}")
        return None


# Example usage:




async def consume_api():
    """Fethcing data"""
    id = input('Enter id:')
    option = input('what action do you want to perform? u = update g = get product d = delete product')

    if option == 'd':
        await delete_product(id)
    elif option == "u":
        update_arg = input('Enter new title on product:')
        await update_product(id, update_arg)
    else:
        await fetchproduct(id)  

  