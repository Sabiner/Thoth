function showArticle(url) {
    $("#blog_content").load("/" + url, "");
}