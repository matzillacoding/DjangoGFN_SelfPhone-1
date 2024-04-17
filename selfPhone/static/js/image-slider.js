// IMAGE SLIDER ON product_details.html

$(document).ready(function(){
    $('.container-product-image').slick({
        dots: true,
        infinite: true,
        autoplay: false,
        responsive: [
            {
                breakpoint: 9999,
                settings: "unslick"
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    })
});

$(window).on('resize orientationchange', function() {
    $('.container-product-image').slick('resize');
});