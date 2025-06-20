import {countProduct} from "./productsCount.js"

// Для того чтоб подключить что-либо из файла -> import {данные} from "./имяФайла.js"
// Перед данными которые будут импортироваться при создании написать export
// Если в js файл что либо будет импортироватьcя его нужно подключать как модуль -> 
// в html теге script - type="module"

const listPlusButton = document.querySelectorAll(".plus")
// for (let переменная of список){} - перебирает список
for (let plusButton of listPlusButton){
    // element.addEventListener - добавляет обработчик события, 
    // (функцию которая работает когда пользователь что-то делает)
    plusButton.addEventListener("click", function(){
        let idProducts = document.cookie.split('=')[1]
        document.cookie = `list_products = ${idProducts}${plusButton.id}|; path = /`
        countProduct(plusButton.id)
    })
    
}