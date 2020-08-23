# AwardWinningFilms
<div>Starting the project with an <a href='https://drive.google.com/file/d/1TwlPVVzWIg5VQ406vSc3ojSuI7Qkm25K/view'>interesting assignment</a> 
  that helps me learn new things.
</div>
<div>The project is made with some crazy stacks (<code>Scrapy</code>, <code>Django</code> and <code>Mongo</code>). 
  <i>Django is not designed for Nosql database.</i>
</div>
<div>But, I tried to taste the flavour.</div>
<div><i>Tested in Linux based OS.</i> After cloning from the repository. Go to the project root directory.</div>

## Run the app with virtual environment using command line
##### Prerequisites
<ul>
  <li>Python3</li>
  <li>Pip3</li>
  <li>Django</li>
  <li>Mongo</li>
</ul>

##### Create and activate Virtual Enviornment with Python3
```
python -m venv venv
```
```
source venv/bin/activate
```

##### Install the requirements
```
pip install -r requirements.txt
```

##### Finally, run the below command
To crawl the Award Winning Films from wikipedia
```
python application.py parse
```
To serve the API
```
python application.py serve
```
#### Now, check the web Server
###### Visit http://127.0.0.1:8080 in your web browser to see the webapp in action!
