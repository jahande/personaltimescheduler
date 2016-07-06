$(document).ready(function () {

    //$("#create_table").numeric();


    $
    $("#create_table").click(
        function () {
            //alert("ddd");
            var colomsNumber = 0 + $("#col").val();
            var rawsNumber = 0 + $("#raw").val();
            var table = new Table(rawsNumber, colomsNumber);
            $('#tableBody').html(table.getHtml());
            table.initializeMouseClickListenners();

        }
    );

});

function Table(rawsNumber, columsNumber) {
    this.columsNumber = columsNumber;
    this.rawsNumber = rawsNumber;
}
Table.prototype.getHtml = function () {
    var str = "";
    for (var i = 0; i < this.rawsNumber; i++) {
        str += "<tr id='" + i + "'>";
        for (var j = 0; j < this.columsNumber; j++) {

            str += "<td id='" + i + "_" + j + "'>1</td>";
        }
        str += "</tr>";
    }
    return str;
};
Table.prototype.initializeMouseClickListenners = function () {
    $("td").click(function () {
        Table.this.text('salam');
    });
};