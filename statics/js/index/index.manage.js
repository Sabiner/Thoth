// Sabiner <chaoyue_ge@163.com>

$(function() {
    $("#blog").click(function () {
        var url = "/load_blog_page";
        load_page(url);
    });
    $("#feedback").click(function () {
        var url = "/feedback";
        load_page(url);
    });
});

layui.use('element', function(){
    var element = layui.element;
});

layui.use(['layer', 'form'], function () {
    var layer = layui.layer, form = layui.form;
});

function load_page(url) {
    $("#content").load(url, '');
}
