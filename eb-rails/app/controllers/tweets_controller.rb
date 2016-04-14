class TweetsController < ApplicationController

  def index
    set_amazon_es

    result = @client.search index: 'place', body: { query: { match_all: {} }, size: 10 }
    @tweets = result['hits']['hits'] #array
    # puts @tweets

  end

  def submit
  end


  skip_before_action :verify_authenticity_token

  # POST /tweets
  def create
    puts request.body.read
    render text: request.body.read
  end

  include ActionController::Live

  def stream

    response.headers['Content-Type'] = 'text/event-stream'
    sse = SSE.new(response.stream, retry: 3000)
    # sse = SSE.new(response.stream, retry: 300, event: "event-name")

    begin

      for i in 0..10
        # sleep 1
        sse.write({ name: 'John'}, id: 10, event: "message", retry: 500)
      end
      # it is in batch

      # Comment.on_change do |data|
      #   sse.write(data)
      # end
    rescue IOError
      # Client Disconnected
    ensure
      sse.close
    end
    # render nothing: true

  end


  private

  def set_amazon_es
    # require 'patron'
    require 'faraday_middleware/aws_signers_v4'
    require 'elasticsearch'


    @client = Elasticsearch::Client.new url: Rails.application.config.es_host do |f|
      f.request :aws_signers_v4,
                credentials: Aws::Credentials.new(Rails.application.config.aws_access_key , Rails.application.config.aws_secret_access_key),
                service_name: 'es',
                region: 'us-east-1'
      # f.adapter :patron
      f.adapter  Faraday.default_adapter
    end

    puts ' + + + + + + + + + + + + + + +  '
    puts ' application.set_amazon_es'
    puts ' + + + + + + + + + + + + + + +  '
  end

  def initialize

  end

end
