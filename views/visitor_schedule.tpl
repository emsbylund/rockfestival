<!DOCTYPE html>
<html>
    <head>
        <title>Rockfestival BLOMSTERMÅLA</title>
        <meta charset="utf-8">
        <link href="/static/style.css" type="text/css" rel="stylesheet">
        <link href='https://fonts.googleapis.com/css?family=Lato:900,400,100' rel='stylesheet' type='text/css'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <header>
            <h1 id="thick">ROCKFESTIVAL</h1><h1 id="thin">BLOMSTERMÅLA</h1>
        </header>
        <hr />
        <div class="left_box">
            <h2>Spelschema</h2>
            <table>
                <tr>
                    <th>Band</th>
                    <th>Datum</th>
                    <th>Startar</th>
                    <th>Slutar</th>
                    <th>Scen</th>
                </tr>
                %for performance in schedule:
                <tr>
                    <td>{{performance[2]}}</td>
                    <td>{{performance[4]}}</td>
                    <td>{{performance[0]}}</td>
                    <td>{{performance[1]}}</td>
                    <td>{{performance[3]}}</td>
                </tr>
                %end

            </table>
        </div>

        <div class="right_box">
            <h2>Bandinformation</h2>
            <table>
                <tr>
                    <th>Band</th>
                    <th>Musikstil</th>
                    <th>Ursprungsland</th>
                </tr>
                %for band in band_info:
                <tr>
                    <td>{{band[0]}}</td>
                    <td>{{band[1]}}</td>
                    <td>{{band[2]}}</td>
                </tr>
                %end
            </table>
        </div>

    </body>
</html>
