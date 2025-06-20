const listButtonDelete = document.querySelectorAll(".delete")

for (let deleteButton of listButtonDelete){
    deleteButton.addEventListener("click", function(){
        let productCookies = document.cookie.split('=')[1]
        // "".replace(), "".replaceAll() - замінює один текст в рядку на інший. (1 текст або всі)
        let cookies = productCookies.replaceAll(`${deleteButton.id}|`, "")
        document.cookie = `list_products = ${cookies}; path = /`
        let product = document.querySelector(`#product-${deleteButton.id}`)
        // elem.remove() - видаляє елемент з сторінки
        product.remove()
    })
}