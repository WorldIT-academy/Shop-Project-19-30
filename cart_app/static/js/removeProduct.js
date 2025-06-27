import { countProduct } from "./productsCount.js";

const listButtonMinus = document.querySelectorAll(".minus")
for (let minusButton of listButtonMinus){
    minusButton.addEventListener("click", function(){
        if (countProduct(minusButton.id) >1){
            let productCookies = document.cookie.split('=')[1]
            let cookies = productCookies.replace(`${minusButton.id}|`, "")
            document.cookie = `list_products = ${cookies}; path = /`
            countProduct(minusButton.id)
        }
    })
}