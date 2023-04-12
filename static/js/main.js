$(document).ready( function () {
    $("#membre_table").DataTable({
        "pageLength": 10,
        "lengthMenu": [5, 10, 20, 30, 50, 70, 100],
        // "processing" : true,
        // "serverSide" : true,
        // "stateSave": true,
        // "stateDuration": 604800, // 604800 secondes = 60 * 60 * 24 * 7 = 7 jours,
        // "order": [0, 'desc'],
        // "scrollCollapse": true,
        "language": {
            "info": "Affichage des membres _START_ à _END_ sur un total de _TOTAL_ membres",
            "search": "Rechercher:",
            "lengthMenu": "Afficher _MENU_ membres",
            "paginate": {
                "first": "Premier",
                "last": "Dernier",
                "next": "Suivant",
                "previous": "Précédent"
            }
        }
    });
    

    $('#cotisation_table').DataTable({
        "pageLength": 10,
        "lengthMenu": [5, 10, 20, 30, 50, 70, 100],
        "language": {
            "info": "Affichage des cotisations _START_ à _END_ sur un total de _TOTAL_ cotisations",
            "search": "Rechercher:",
            "lengthMenu": "Afficher _MENU_ cotisations",
            "paginate": {
                "first": "Premier",
                "last": "Dernier",
                "next": "Suivant",
                "previous": "Précédent"
            },
        }
    });
    
    $('#commission_table').DataTable({
        "pageLength": 10,
        "lengthMenu": [5, 10, 20, 30, 50, 70, 100],
        "language": {
            "info": "Affichage des commissions _START_ à _END_ sur un total de _TOTAL_ commissions",
            "search": "Rechercher:",
            "lengthMenu": "Afficher _MENU_ commissions",
            "paginate": {
                "first": "Premier",
                "last": "Dernier",
                "next": "Suivant",
                "previous": "Précédent"
            },
        },
    });
});
