require 'json'

class TweetsController < ApplicationController

  def search
    indexstr = 'foo'

    keyword = params[:keyword] || 'all'
    puts keyword

    set_amazon_es
    if keyword == 'all'
      result = @es_client.search index: indexstr, body: { query: { match_all: { } }, size: 5 }
    else
      result = @es_client.search index: indexstr, body: { filter: { type: { value: keyword } }, size: 10 }
    end

    @filteredTweets = result['hits']['hits'] #array

  end



  skip_before_action :verify_authenticity_token

  # POST /tweets
  def create

    data =  request.body.read
    json = JSON.parse(data)
    message =  JSON.parse(json['Message'])

    send_to_es message

    render text: 'hi'
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

    def send_to_es(newtweet)
      set_amazon_es

      trackList = ['concert', 'trip', 'running', 'party']
      indexstr = 'foo'

      isFound = false #~~
      trackList.each do |type|
        if newtweet['tweet'].downcase.include? type
          @es_client.index  index: indexstr, type: type, body: newtweet
          puts type
          isFound = true
          break
        end
      end
      if !isFound
        puts newtweet['tweet']
      end

    end



end
