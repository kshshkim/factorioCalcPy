let rand = Math.random()

function setCookie () {
    document.cookie = "rand_id="+rand.toString()
}

function getCookie (key) {
    let ck = document.cookie
    ck = ck.replace(" ", "")
    let cksp = ck.split(';')
    let to_return = ""
    for (let cckk in cksp){
        let knv = cksp[cckk].split("=")
        if (knv[0] === key){
            to_return = knv[1]
            break
        }
    }
    return to_return
}

function sendJsonReq(postOrGet, to_where, data) {
    $.ajax({
        url: to_where,
        type: postOrGet,
        dataType: "json",
        data: JSON.stringify(data),
        contentType: "application/json, charset=UTF-8"
    })
}

function sendRandID(to_where){
    let to_send = {"rand_id": rand}
    sendJsonReq("POST", to_where, to_send)
}

function set_session(){
    if (getCookie("rand_id") !== ""){
        rand = Number(getCookie("rand_id"))
    } else {
        setCookie()
    }
    sendRandID("/session")
    startUpdate = setInterval(function () {
        sendRandID("/session/imalive")
        }, 10000)

}