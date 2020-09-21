<?php

$filename = "feed-articles.csv";
$csvArray = ImportCSV2Array($filename);

echo '<div class="container" style="margin-bottom: 75px;">';
echo '<h2>Recent articles related to MTC</h2>';
echo '<ul class="list-group">';

// try to sort this thing:
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

// This parses out the Google Alerts referring URL/parameter, and strips it down to just the subdomain and tld. //
						$url_components = parse_url($row['post.link']);
						parse_str($url_components['query'], $params);
						$cleanURL = $params['url'];

						$tmp = explode("/", $cleanURL);
						$domain = $tmp[2];

						if (strpos($domain, "www") === 0) {
						    //Starts with www.
						    $domain = substr($domain, 4);
						}

						echo '<p>';
						echo 'Domain: <b>' . $domain;
						echo '</b></p>';

//echo ' 				<p>Link: ' . $row['post.link'] . ' </p>';
echo '            <a href="' . $row['post.link'] . '" target="_blank">';
echo '            <button type="button" class="btn btn-primary">Full article</button></a>';
// **Strongly suggest securing this button or the next page with a login or validation of some sort to prevent malicous use** //
echo '            <a href="https://medullarythyroidcancer.org/news/blacklist-domain.php?domain=' . $domain . '">';
echo '            <button type="button" class="btn btn-danger">Blacklist Domain</button></a>';

echo '           </div>
              </div>
            </div>
          </div>
        </div>';
}

echo '</ul>';
echo '</div>';

?>
