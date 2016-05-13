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
        <div id="wrapper">
            <header>

                <h1 id="thick">ROCKFESTIVAL</h1><h1 id="thin">BLOMSTERMÅLA</h1>
                <nav>
                    <ul>
                        <li><a href="/schedule">Spelschema</a> </li>
                        <li><a href="/festival_workers">Festivalarbetare</a></li>
                        <li><a href="">Chefer</a></li>
                        <li><a href="">Band</a> </li>
                        <li><a href="">Säkerhetsansvarig</a></li>
                    </ul>
                </nav>
            </header>

            <div id="content">
                <div class="left_box">
                    <h2>Spelschema</h2>
                    <table border="1px solid black">
                        <tr>
                            <th>Band</th>
                            <th>Startar</th>
                            <th>Slutar</th>
                            <th>Scen</th>
                        </tr>
                        %for performance in schedule:
                        <tr>
                            <td>{{performance[2]}}</td>
                            <td>{{performance[0]}}</td>
                            <td>{{performance[1]}}</td>
                            <td>{{performance[3]}}</td>
                        </tr>
                        %end
                    </table>
                </div>
                <div class="right_box">
                    <h2>Lägg till nytt framträdande</h2>
                    <form name="add_performance" id="add_performance" method="POST" action="">
                        <select name="choose_band" form="add_performance" value="">
                            <option>Välj band</option>
                            <option>Band 1</option>
                            <option>Band 2</option>
                            <option>Band 3</option>
                        </select>
                        <select name="choose_stage" form="add_performance">
                            <option>Välj scen</option>
                            <option>Scen 1</option>
                            <option>Scen 2</option>
                            <option>Scen 3</option>
                        </select>
                        <label for="add_start_time">Starttid:</label>
                        <input type="input" name="add_start_time" id="add_start_time" placeholder="hh:mm:ss">
                        <label for="add_finish_time">Sluttid:</label>
                        <input type="input" name="add_finish_time" id="add_finish_time" placeholder="hh:mm:ss">
                        <input type="submit" name="add_performance_submit" id="add_performance_submit" value="Spara">
                    </form>
                </div>
            </div>

            <footer>

            </footer>
        </div>
    </body>
</html>
