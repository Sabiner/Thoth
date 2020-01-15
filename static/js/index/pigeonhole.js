$(document).ready(function () {
    $('.navlist li').click(function () {
        $(this).addClass('navcurrent').siblings().removeClass('navcurrent');
        $('.navtab>div:eq(' + $(this).index() + ')').show().siblings().hide();
    });
});
