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
                    <li><a href="">Säkerhetsansvarig</a></li>
                </ul>
            </nav>
        </header>
    

        <div id="wrapper">
            <div class="right_box">
                <h2>Festivaljobbare
                <span>Kontaktuppgifter</span></h2>
                      <table>
                        <tr>
                            <th>Namn</th>
                            <th>Telefon Nr</th>
                            <th>Person Nr</th>
                            <th>Ansvarig Chef</th>
    
                        </tr>
                        %for worker in festivaljobbare:
                        <tr>
                            <td>{{worker[1]}}</td>
                            <td>0{{worker[2]}}</td>
                            <td>{{worker[0]}}</td>
                            <td>{{worker[3]}}</td>
                          </tr>
                        %end
                    </table>
            </div>
            <div class="left_box">
                    <form name="add_worker"  method="POST" action="/add_new_worker/" class="dark-matter">
                        
                <h1>Lägg till ny festivaljobbare
        <span>Var god att fyll i alla fälten.</span>
                </h1>
                Festivaljobbare:<br>
                <input type="text" name="name" placeholder="Skriv namn & efternamn här"><br>
                Telefon Nr:<br>
                <input type="text" max="10" min="7" name="TelNr" placeholder="Skriv ditt telefon nr här"><br>
                Person Nr:<br>
                <input type="text" name="bday" min="10" max="10" placeholder="ååmmddxxxx"><br>
                        
                Välj ansvarig chef:<br>
                <select name="choose_chef" form="add_worker">  
                            %for name in chef:
                        
                            <option>{{name[0]}}</option>
                            %end
                        </select><br>
                <input class="button" type="submit" value="Lägg till">
            </form>
                
            </div>
        </div>

        <footer>

        </footer>
    </body>
</html>
