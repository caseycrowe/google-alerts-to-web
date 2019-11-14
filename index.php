<?php

// This file uses Bootstrap 4.0 for CSS/Style. You can use whatever style you like. 
// https://getbootstrap.com/docs/4.3/getting-started/introduction/

$filename = "feed_articles.csv";
$csvArray = ImportCSV2Array($filename);

echo '<div class="container">';
echo '<h2>Recent articles related to <subject></h2>';
echo '<ul class="list-group">';

// Sort the results:
function cmp($a, $b)
{
    return strcmp(intval($b["date"]), intval($a["date"]));
}
usort($csvArray, "cmp");


foreach ($csvArray as $row){
echo '  <div class="row">
          <div class="col-lg-12">
            <div class="bs-component">
              <div class="card border-primary mb-3" <!--style="max-width: 20rem;-->">';
echo '                <div class="card-header">Published:  ' . date("M jS, Y g:i A", $row['date']) . '</div>';
echo '                 <div class="card-body">
                  <h4 class="card-title">' . $row['post.title'] . '</h4>';
echo '                  <p class="card-text">"' . $row['post.content.value'] . '"</p>';
echo '            <a href="' . $row['post.link'] . '" target="_blank">';
echo '            <button type="button" class="btn btn-primary">Full article</button></a>';
echo '           </div>
              </div>
            </div>
          </div>
        </div>';
}

echo '</ul>';
echo '</div>';

?>
