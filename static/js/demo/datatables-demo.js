$(document).ready(function() {
  // Options communes
  const commonOptions = {
    language: {
      search: "Rechercher",
      searchPlaceholder: "Search...",
      lengthMenu: "Afficher _MENU_ entrées",
      paginate: {
        previous: "Précédent",
        next: "Suivant"
      }
    }
  };

  // Initialisation des DataTables
  $('#dataTable').DataTable(commonOptions);

  /* Page de rapports */
  $('.dataTable_actif').DataTable(commonOptions); 

  /* Fin page de rapport */
});