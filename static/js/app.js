let des = document.querySelector('#des')
let btn = document.getElementById('btn')
let save = document.getElementById('save')
let room = document.getElementById('room')

save.addEventListener('click', (e) => {
    e.preventDefault()
    des.style.display = 'block'
    room.style.display = 'none'
    btn.style.display = 'block'
    console.log('something went wrong')
})



// btn.addEventListener('click', (e) => {
//     e.preventDefault()
//     des.style.display = 'none'
//     room.style.display = 'block'
//     btn.style.display = 'none'
//     console.log('something went wrong')
// })
