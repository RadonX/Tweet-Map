class MainController < ApplicationController

  def show
    keyword = params[:keyword] || 'all'
    puts keyword

    @indexstr = 'foo'

    set_amazon_es
    if keyword == 'all'
      result = @es_client.search index: @indexstr, body: { query: { match_all: { } }, size: 50 }
    else
      result = @es_client.search index: @indexstr, body: { filter: { type: { value: keyword } }, size: 50 }
    end

    @filteredTweets = result['hits']['hits'] #array
  end

end
