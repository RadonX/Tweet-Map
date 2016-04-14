  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="description" content="">
  <meta name="author" content="">
  <!--link rel="icon" href="../../favicon.ico"-->


  <!-- Custom styles for this template -->
  <link href="static/css/dashboard.css" rel="stylesheet">

<!--script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script-->
<script src="static/js/bootstrap.min.js"></script>


---


### Rails

//= require turbolinks
//= require_tree .

http://guides.rubyonrails.org/asset_pipeline.html


<% content_for :bodyfoot do %>
    <%= javascript_include_tag '/assets/map', async: true, defer: true %>
<% end %>


Active Record??

### Ruby

what's  `patron`


The best practice for ingesting Tweets and other streaming messages is to decouple collection and processing of high volume streams. For example, collect the raw text of messages in one process, passing each message into a message queue, rotated flatfile, or database. A second process or set of processes should parse the messages and extract any necessary fields for storage or further manipulation.

---

#### todo

1. hide key info before git push

trackList = ['concert', 'trip', 'running', 'party']
index
new(ENV['AWS_ACCESS_KEY'], ENV['AWS_SECRET_ACCESS_KEY']),

arn:aws:sns:us-east-1:664206762806:entertainment



[Getting Started with Elasticsearch on Rails](http://www.codinginthecrease.com/news_article/show/409843?referrer_id=948927)
http://www.sitepoint.com/full-text-search-rails-elasticsearch/

2. Never trust parameters from the scary internet, only allow the white list through.

       def tweet_params
         params.fetch(:tweet, {})
       end

  def index
    @users = User.all
    respond_to do |format|
      format.html # index.html.erb
      format.xml  { render xml: @users}
      format.json { render json: @users}
    end
  end

3. # Do not keep production secrets in the repository,
   # instead read values from the environment.
   production:
     secret_key_base: <%= ENV["SECRET_KEY_BASE"] %>


# signal.pause()

4. set_amazon_es
    class static in application_controller , not instance


5. page is re rendered
   save data directly

6. delete main#home



#### possible problems

1. Amazon EC access policy

2. [asset not precompiled in rails 3 | codedecoder](https://codedecoder.wordpress.com/2012/11/05/asset-not-precompiled-asset_pipeline-rails-3/)

#### Reference

1. [Document accessing the AWS Elasticsearch Service using IAM credentials · Issue #232 · elastic/elasticsearch-ruby](https://github.com/elastic/elasticsearch-ruby/issues/232)

2. https://github.com/rails/jbuilder

3. [ActionController::Live::SSE](http://api.rubyonrails.org/classes/ActionController/Live/SSE.html)



---


{"user"=>"Mary Roeder",
"sentiment"=>{"type"=>"negative", "score"=>"-0.284899"},
"geo"=>"{'coordinates': [-83.73524, 42.27497], 'type': 'Point'}",
"tweet"=>"Someone's running a side hustle out of the UMS Production office.  \n\n#mnozilbrass #umslobby… https://t.co/3lzZkvHE8r"}


---

https://docs.google.com/forms/d/1XZzrDsDdpsvzWRn3KIEmgbYMv_FK0eIsQD5bZyavoMM/viewform?usp=form_confirm


var points = [{&quot;_index&quot;=&gt;&quot;.kibana-4&quot;, &quot;_type&quot;=&gt;&quot;index-pattern&quot;, &quot;_id&quot;=&gt;&quot;posts*&quot;, &quot;_score&quot;=&gt;1.0, &quot;_source&quot;=&gt;{&quot;title&quot;=&gt;&quot;posts*&quot;, &quot;customFormats&quot;=&gt;&quot;{}&quot;, &quot;fields&quot;=&gt;&quot;[{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_index\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;author\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;topics\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_type\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;blog\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;title\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;number\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;awesomeness\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_source\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_id\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false}]&quot;}}, {&quot;_index&quot;=&gt;&quot;.kibana-4&quot;, &quot;_type&quot;=&gt;&quot;config&quot;, &quot;_id&quot;=&gt;&quot;4.0.3&quot;, &quot;_score&quot;=&gt;1.0, &quot;_source&quot;=&gt;{&quot;buildNum&quot;=&gt;6103, &quot;defaultIndex&quot;=&gt;&quot;twit3*&quot;}}, {&quot;_index&quot;=&gt;&quot;.kibana-4&quot;, &quot;_type&quot;=&gt;&quot;index-pattern&quot;, &quot;_id&quot;=&gt;&quot;twit3*&quot;, &quot;_score&quot;=&gt;1.0, &quot;_source&quot;=&gt;{&quot;title&quot;=&gt;&quot;twit3*&quot;, &quot;customFormats&quot;=&gt;&quot;{}&quot;, &quot;fields&quot;=&gt;&quot;[{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;user.location\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;number\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.bounding_box.coordinates\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_index\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;number\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;geo.coordinates\&quot;,\&quot;count\&quot;:1,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;user.name\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.url\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.full_name\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;created_at\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.country\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.place_type\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.country_code\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;coordinates.type\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;text\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;geo.type\&quot;,\&quot;count\&quot;:6,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.name\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;number\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;user.id\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_type\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.bounding_box.type\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:true,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;place.id\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;number\&quot;,\&quot;indexed\&quot;:true,\&quot;analyzed\&quot;:false,\&quot;doc_values\&quot;:false,\&quot;name\&quot;:\&quot;coordinates.coordinates\&quot;,\&quot;count\&quot;:1,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_source\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false},{\&quot;type\&quot;:\&quot;string\&quot;,\&quot;indexed\&quot;:false,\&quot;analyzed\&quot;:false,\&quot;name\&quot;:\&quot;_id\&quot;,\&quot;count\&quot;:0,\&quot;scripted\&quot;:false}]&quot;}}, {&quot;_index&quot;=&gt;&quot;foo&quot;, &quot;_type&quot;=&gt;&quot;party&quot;, &quot;_id&quot;=&gt;&quot;AVQSXR1cJ5wQa8uglXfC&quot;, &quot;_score&quot;=&gt;1.0, &quot;_source&quot;=&gt;{&quot;sentiment&quot;=&gt;{&quot;type&quot;=&gt;&quot;neutral&quot;}, &quot;geo&quot;=&gt;{&quot;coordinates&quot;=&gt;[-86.86604, 35.92263], &quot;type&quot;=&gt;&quot;Point&quot;}, &quot;user&quot;=&gt;&quot;Legendary Kimbros&quot;, &quot;tweet&quot;=&gt;&quot;Paul Kramer &amp;amp; Swing Street tonight at 6 followed by @musiccityroots after party at 9:30!… https://t.co/Orkv3LXEoU&quot;}}, {&quot;_index&quot;=&gt;&quot;foo&quot;, &quot;_type&quot;=&gt;&quot;running&quot;, &quot;_id&quot;=&gt;&quot;AVQSX1ykJ5wQa8uglXfF&quot;, &quot;_score&quot;=&gt;1.0, &quot;_source&quot;=&gt;{&quot;sentiment&quot;=&gt;{&quot;type&quot;=&gt;&quot;neutral&quot;}, &quot;user&quot;=&gt;&quot;Andrzej Brylka&quot;, &quot;geo&quot;=&gt;{&quot;type&quot;=&gt;&quot;Point&quot;, &quot;coordinates&quot;=&gt;[18.5298948, 54.5534645]}, &quot;tweet&quot;=&gt;&quot;I just finished running 0.86 km in 5m:40s with #Endomondo #endorphins https://t.co/79AnFXmdiM&quot;}}] ;



