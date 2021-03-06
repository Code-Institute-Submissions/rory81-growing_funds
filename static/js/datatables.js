$(document).ready(function() {
    $('#myTable').dataTable({
        "pageLength":5,
        "lengthMenu":[2,5,10,25,50],
        "columnDefs": [{ "width": "40%", "targets": 0 }]
    });
} );


$(document).ready(function() {
    $('#myHistoryTable').dataTable({
        "pageLength":5,
        "lengthMenu":[5,10,25,50],
        "columnDefs": [{ "width": "25%", "targets": 0 }]
    } );
} );


$(document).ready(function() {
    $('#myProjectsTable').dataTable({
        "pageLength":5,
        "lengthMenu":[5,10,25,50],
        "columnDefs": [{ "width": "30%", "targets": 0 }],
    } );
} );

$(document).ready(function() {
    $('#searchProjectsTable').dataTable({
        "pageLength":5,
        "lengthMenu":[5,10,25,50],
        "columnDefs": [{ "width": "35%", "targets": 0 }],
        searching: false,
    } );

} );
