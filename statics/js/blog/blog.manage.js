function showArticle(url) {
    $("#blog_content").load("/" + url, "");
}

function showTag(type_name) {
    var url = "/show_type?type=" + type_name;
    $("#content").load(url);
}