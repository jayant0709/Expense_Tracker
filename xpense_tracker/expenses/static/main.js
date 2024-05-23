// Sticky Navbar
$(window).scroll(function () {
    if ($(this).scrollTop() > 90) {
        $('.nav-bar').addClass('sticky-top shadow');
    } else {
        $('.nav-bar').removeClass('sticky-top shadow');
    }
});

// Dropdown on mouse hover
const $dropdown = $(".dropdown");
const $dropdownToggle = $(".dropdown-toggle");
const $dropdownMenu = $(".dropdown-menu");
const showClass = "show";

$(window).on("load resize", function() {
    if (this.matchMedia("(min-width: 992px)").matches) {
        $dropdown.hover(
        function() {
            const $this = $(this);
            $this.addClass(showClass);
            $this.find($dropdownToggle).attr("aria-expanded", "true");
            $this.find($dropdownMenu).addClass(showClass);
        },
        function() {
            const $this = $(this);
            $this.removeClass(showClass);
            $this.find($dropdownToggle).attr("aria-expanded", "false");
            $this.find($dropdownMenu).removeClass(showClass);
        }
        );
    } else {
        $dropdown.off("mouseenter mouseleave");
    }
});


// Back to top button
$(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
});
$('.back-to-top').click(function () {
    $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
    return false;
});

// Delete Account
function deleteAccount() {
    var username = document.querySelector('.user-info strong').textContent;

    $.ajax({
        type: 'POST',
        url: '/remove_user/',  
        data: {
            'username': username
        },
        success: function(response) {
            if (response.success) {
                console.log(response.message);  
            } else {
                console.log(response.message);  
            }
        },
        error: function(xhr, status, error) {
            console.error('AJAX request failed:', error);  
        }
    });
}

document.getElementById('delete-account-form').addEventListener('submit', function(e) {
    e.preventDefault();
    console.log('Form submitted');
    this.submit();
});
