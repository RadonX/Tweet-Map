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

    render text: "hello, world!"

---


### Rails

//= require turbolinks
//= require_tree .

http://guides.rubyonrails.org/asset_pipeline.html

### Ruby

    client.index  index: 'myindex', type: 'mytype', id: 1, body: { title: 'Test' }
# => {"_index"=>"myindex", ... "created"=>true}

what's patron
---

#### todo

1. hide key info before git push

new(ENV['AWS_ACCESS_KEY'], ENV['AWS_SECRET_ACCESS_KEY']),

arn:aws:sns:us-east-1:664206762806:entertainment

http://stackoverflow.com/questions/20857886/where-can-i-store-site-wide-variables-in-rails-4


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

#### possible problems

1. Amazon EC access policy


#### Reference

1. [Document accessing the AWS Elasticsearch Service using IAM credentials · Issue #232 · elastic/elasticsearch-ruby](https://github.com/elastic/elasticsearch-ruby/issues/232)

2. https://github.com/rails/jbuilder

3. [ActionController::Live::SSE](http://api.rubyonrails.org/classes/ActionController/Live/SSE.html)