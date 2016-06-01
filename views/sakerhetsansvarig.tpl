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
    

        <div id="wrapper">
            <div class="left-box">
                <h2>Säkerhetsansvarig</h2>
                      <table>
                        <tr>
                            <th>Festivaljobbare</th>
                            <th>Startdatum</th>
                            <th>Slutdatum</th>
                            <th>Starttid</th>
                            <th>Sluttid</th>
                            <th>Scen</th>
                            
    
                        </tr>
                        %for worker in securityworker:
                        <tr>
                            <td>{{worker[5]}}</td>
                            <td>{{worker[1]}}</td>
                            <td>{{worker[3]}}</td>
                            <td>{{worker[2]}}</td>
                            <td>{{worker[4]}}</td>
                            <td>{{worker[0]}}</td>
                            
                          </tr>
                        %end
                    </table>
            </div>
            
            <div class="right_box">
                    <h2>Lägg till ny säkerhetsansvarig</h2>
                    <form name="add_security" id="add_security" method="POST" action="/add_new_security" class="dark-matter">
                        <select name="choose_worker" form="add_security" value="">
                            <option>Välj festivaljobbare</option>
                            %for workers in list_of_workers:
                                <option>{{workers[0]}}</option>
                            %end
                        </select>
                        <select name="choose_stage" form="add_performance">
                            <option>Välj scen</option>
                            %for stage in stages:
                                <option>{{stage[0]}}</option>
                            %end
                        </select>
                        
                        <label for="date_for_show">Startdatum: </label>
                        <input type="input" name="start_date" id="start_date" placeholder="åååå-mm-dd">
                        <label for="date_for_show">Slutdatum: </label>
                        <input type="input" name="end_date" id="end_date" placeholder="åååå-mm-dd">
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
    </body>
</html>
