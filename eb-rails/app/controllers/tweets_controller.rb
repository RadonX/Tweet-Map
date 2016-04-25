require 'json'
require 'sse_manager'

class TweetsController < ApplicationController

  def search

    # the same to main#show
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

    #json
  end



  skip_before_action :verify_authenticity_token

  # POST /tweets
  def create
    data =  request.body.read
    puts data
    ## no implementation of SNS subscription. check the log to subscript manually
    json = JSON.parse(data)
    message =  JSON.parse(json['Message'])
    send_to_es message
    SSEManager.publish message['tweet']
    render nothing: true
  end


  # Needed for response.stream/SSE
  include ActionController::Live

  def stream
    id = params[:id]
    msg = SSEManager.get_msg(id)
    response.headers['Content-Type'] = 'text/event-stream'
    sse = SSE.new(response.stream, retry: 5000, event: "message")
    begin
      if msg
        sse.write(msg)
      else
        render nothing: true
      end
    rescue IOError
    ensure
      sse.close
    end

  end

  private

  TRACKLIST = ['concert', 'trip', 'running', 'party']

  def send_to_es(newtweet)
      set_amazon_es
      isFound = false
      TRACKLIST.each do |type|
        if newtweet['tweet'].downcase.include? type
          @es_client.index  index: Rails.application.config.es_index, type: type, body: newtweet
          puts type
          isFound = true
          break
        end
      end
      if !isFound # the coming tweet doesn't belong to any of the types
        puts newtweet['tweet']
      end
    end

end
