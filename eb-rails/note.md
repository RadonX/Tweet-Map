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

6. delete main#show


#render text: 'hi'



#### possible problems

1. Amazon EC access policy

2. [asset not precompiled in rails 3 | codedecoder](https://codedecoder.wordpress.com/2012/11/05/asset-not-precompiled-asset_pipeline-rails-3/)

3. In SSE stream, don't render anything. Say, not to write `render nothing: true`.


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



