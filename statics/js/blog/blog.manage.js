function showArticle(url) {
    console.log(url);
    $("#blog_content").load("/" + url, "");
}