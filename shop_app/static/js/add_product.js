
const listBuyButtons = document.querySelectorAll(".buy-buttons")


for (let count = 0; count<listBuyButtons.length; count++){
    let button = listBuyButtons[count]
    button.addEventListener(type="click", listener=function(){
        if(document.cookie == ""){
            document.cookie = `list_products = ${button.id}|; path=/`
        }else{
            let productsId = document.cookie.split("=")[1]
            document.cookie = `list_products = ${productsId}${button.id}|; path=/`
        }
    })
}