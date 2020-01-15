/**
 * 主页相关数据初始化加载
 */

function load_page() {
    load_recommend();           // 推荐
    load_ranking_list();        // 排行榜
    load_correlation_list();    // 相关列表
}

function load_recommend() {
    let url = "/article/get_latest_article";
    $("#content").load(url, "");
}

function load_ranking_list() {
    let url = "/article/get_ranking_list";
    $("#ms-main").load(url, "");
}

function load_correlation_list() {
    let url = "/article/get_correlation";
    $("#correlation").load(url, "");
}

function switch_tag(obj) {
    $("#topnav_current").removeAttr("id");
    $(obj).attr("id", "topnav_current");
}

/**
 * 关于我
 */
function about_me() {
    let url = "/about_me";
    $("article").load(url, "");
}

/**
 * 加载留言板界面
 */
function message_board() {
    $("article").load("/guestbook/message_board", "");
    load_guest_book();
}

/**
 * 归档
 */
function pigeonhole() {
    let url = "/pigeonhole";
    $("article").load(url, "");
}

/**
 * 留言
 */
function leave_word() {
    let message = $("textarea").val();
    $.ajax({
        type: 'POST',
        url: "/guestbook/leave_word",
        data: {
            message: message
        },
        success: function (data) {
            load_guest_book();
        },
        error: function (xhr,state,errorThrown) {
            console.log(errorThrown);
        }
    });
}

/**
 * 加载留言板最新内容
 */
function load_guest_book() {
    $(function(){
     $.ajax({
            type: "GET",
            url: "/guestbook/load_guest_book",
            success:function(msg){
                $("#guestbook").html(msg);
            },
            error:function(XMLHttpRequest, textStatus, thrownError){}
        })
    })
}