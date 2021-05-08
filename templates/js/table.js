    /*
 *
 *@param {tableId} contines table name
 *
 */
 function createTable(tableID, content) {
    for (var i = 0; i < 9; i++) {
        var x = i + 8;
        var tr = document.createElement('tr');
        tr.className = "tr-style";
        var td = document.createElement('td');
        td.className = "tr-style";
        td.style.width = "80px";

        // x = "<tr style='height: 30px; border-style: solid;'>" + x + "</tr>";

        td.innerHTML = x + ":00";
        tr.appendChild(td);
        document.getElementById(tableID).appendChild(tr);
        if (i == 0) {
            var div = document.createElement('div');
            div.id = content;
            div.style.width = "828px";
            div.style.height = "736px";
            div.style.position = "relative";
            td = document.createElement('td');
            td.colSpan = 5;
            td.rowSpan = 9;

            td.appendChild(div)
            tr.appendChild(td);
            document.getElementById(tableID).appendChild(tr);
        }

    }
}

/*
 *
 *@param {data} dectionary variable contain one level table it should be like mokdata
 *data = [
 *  {
 *   "table_name":"CS",
 *   "course_id":"ARAB101",
 *   "hall_id":"1",
 *   "start_time":"8",
 *   "end_time":"9.5",
 *   "day":"1",
 *   "level":"1",
 *   "instrctor_id":"1"
 *  },
 * ]
 *@param {tableId} contines table name
 *
 */
function addDataToTable(data, tableId, content) {
    createTable(tableId, content)
    var colors = ["#ffc93c", "#c0e218", "#ffab73", "#e9b0df", "#ec4646", "#eeebdd", "#e48900", "#9ede73"]
    var color = ""
    var height = 81;
    var width = 162;

    // object should
    var table_list = []
    for (var i = 0; i < 8; i++) {
        table_list.push([])
        for (var j = 0; j < 5; j++) {
            table_list[i].push("")
        }
    }
    for (var i = 0; i < data.length; i++) {
        //===================convert time===============
        const start_time = data[i].start_time;
        const end_time = data[i].end_time;
        const h_start_time = Math.floor(start_time);
        const m_start_time = (start_time - Math.floor(start_time)) * 60;
        const h_end_time = Math.floor(data[i].end_time);
        const m_end_time = (end_time - Math.floor(end_time)) * 60;
        //===================list block==================                                
        const tr1 = document.createElement("tr");
        const tr3 = document.createElement("tr");
        const tr4 = document.createElement("tr");
        const td1 = document.createElement("td");
        const td2 = document.createElement("td");
        const td3 = document.createElement("td");
        const td4 = document.createElement("td");
        const table = document.createElement("table");
        table.style.fontWeight = "bold";
        table.style.borderStyle = "none";
        table.style.textAlign = "center";
        td1.style.borderStyle = "none";
        td2.style.borderStyle = "none";
        td3.style.borderStyle = "none";
        td4.style.borderStyle = "none";
        tr1.style.borderStyle = "none";
        tr3.style.borderStyle = "none";
        tr4.style.borderStyle = "none";

        //---------------
        td1.innerHTML = data[i].course_id;
        td1.colSpan = 2;
        tr1.appendChild(td1);
        table.appendChild(tr1);
        //---------------
        td2.innerHTML = data[i].instructor;
        tr4.appendChild(td2);
        //---------------
        td3.innerHTML = h_start_time + ":" + m_start_time + " - " + h_end_time + ":" + m_end_time;
        td3.colSpan = 2;
        tr3.appendChild(td3);
        table.appendChild(tr3);
        //---------------
        td4.innerHTML =  "Hall:" + data[i].hall_id;
        tr4.appendChild(td4);
        table.appendChild(tr4);
        //---------------
        //td5.innerHTML = "level: " + data[i].level;
        //tr4.appendChild(td5);

        //===================choose same color for same course=========
        color = colors[i % 8]
        for (var j = 0; j < i; j++){
            if (data[i].course_id  === data[j].course_id){
                color = colors[j % 8];
            }
        }


            //=================== div block =================
        const div = document.createElement('div');
        div.className = "div-course";
        //===================                         
        div.style.backgroundColor = color;
        div.style.position = "absolute";

        const x = (data[i].day - 1) * (width + 2) + (data[i].day - 1) * 1.5;
        const y = (start_time - 8) * (height + 1);
        console.log(x + "  " + y);

        div.style.left = x + "px";
        div.style.top = y + "px";
        const h = (end_time - start_time) * (height - 1);

        div.style.width = width + "px";
        div.style.height = h + "px";
        div.style.textAlign = "-webkit-center";

        //===================
        div.appendChild(table);
        document.getElementById(content).appendChild(div);

    }

}

/*
 *
 * pagination through the tables
 *
 */

var paginationHandler = function () {
    // store pagination container so we only select it once
    var $paginationContainer = $(".pagination-container"),
        $pagination = $paginationContainer.find('.pagination ul');
    // click event
    $pagination.find("li a").on('click.pageChange', function (e) {
        e.preventDefault();
        // get parent li's data-page attribute and current page
        var parentLiPage = $(this).parent('li').data("page"),
            currentPage = parseInt($(".pagination-container div[data-page]:visible").data('page')),
            numPages = $paginationContainer.find("div[data-page]").length;
        // make sure they aren't clicking the current page
        if (parseInt(parentLiPage) !== parseInt(currentPage)) {
            // hide the current page
            $paginationContainer.find("div[data-page]:visible").hide();
            if (parentLiPage === '+') {
                // next page
                $paginationContainer.find("div[data-page=" + (currentPage + 1 > numPages ? numPages : currentPage + 1) + "]").show();
            } else if (parentLiPage === '-') {
                // previous page
                $paginationContainer.find("div[data-page=" + (currentPage - 1 < 1 ? 1 : currentPage - 1) + "]").show();
            } else {
                // specific page
                $paginationContainer.find("div[data-page=" + parseInt(parentLiPage) + "]").show();
            }
        }
    });
};