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
                        <li><a href="/show_security">Säkerhetsansvarig</a></li>
                    </ul>
                </nav>
            </header>

            <div id="content">
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
                    <h2>Lägg till nytt framträdande</h2>
                    <form name="add_performance" id="add_performance" method="POST" action="/add_new_performance" class="dark-matter">
                        <select name="choose_band" form="add_performance" value="">
                            <option>Välj band</option>
                            %for band in list_of_bands:
                                <option>{{band[0]}}</option>
                            %end
                        </select>
                        <select name="choose_stage" form="add_performance">
                            <option>Välj scen</option>
                            %for stage in stages:
                                <option>{{stage[0]}}</option>
                            %end
                        </select>
                        <label for="add_start_time">Starttid:</label>
                        <input type="input" name="add_start_time" id="add_start_time" placeholder="hh:mm:ss">
                        <label for="add_finish_time">Sluttid:</label>
                        <input type="input" name="add_finish_time" id="add_finish_time" placeholder="hh:mm:ss">
                        <label for="date_for_show">Datum: </label>
                        <input type="input" name="date_for_show" id="date_for_show" placeholder="åååå-mm-dd">
                        <input type="submit" name="add_performance_submit" id="add_performance_submit" value="Spara" class="button">
                    </form>
                </div>
            </div>

            <footer>

            </footer>
        </div>
    </body>
</html>
