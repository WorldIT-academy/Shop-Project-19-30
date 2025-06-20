
export function countProduct(productId){
    let productCookies = document.cookie.split('=')[1]
    let listProducts = productCookies.split("|") 
    let count = 0
    for (let id of listProducts){
        if (productId == id ){
            count += 1
        }
    }
    let text = document.querySelector(`#count-${productId}`)
    text.textContent = count 
    return count 
}