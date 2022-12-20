
$(() => {
 
    anime({
        targets: '#right-col',
        right: '0px',
        duration: 1800,
        easing: 'easeInOutQuad'
     })




     anime({
        targets: 'footer svg',
        left: '300px',
        duration: 1800,
        easing: 'easeInOutQuad'
     })


     $('#logo img, #logo span').fadeIn(900)


     $(window).resize(() => {
        if($(window).width() <= 1024){
           let p = document.createElement('p')
           let hamburgerHTMLEntity = document.createTextNode('☰')
           p.appendChild(hamburgerHTMLEntity)
           let hamburgerMenuButton = document.createElement('div')
           //let nav = document.createElement('nav')
           hamburgerMenuButton.setAttribute('class', 'menu-button')
           hamburgerMenuButton.appendChild(p)
           //nav.appendChild(hamburgerMenuButton)
           //$('nav').html(hamburgerMenuButton)
           $('nav').html(hamburgerMenuButton)
           $('nav ul').hide()
         }
         else {
           $('nav div').remove()


         }
     })

     
})


