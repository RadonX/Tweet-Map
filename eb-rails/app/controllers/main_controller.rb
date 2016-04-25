require 'sse_manager'

class MainController < ApplicationController

  def show
    keyword = params[:keyword] || 'all'

    # search for specific type of tweets on ElasticSearch, size limit to 50
    set_amazon_es
    if keyword == 'all'
      result = @es_client.search index: Rails.application.config.es_index, body: { query: { match_all: { } }, size: 50 }
    else
      result = @es_client.search index: Rails.application.config.es_index, body: { filter: { type: { value: keyword } }, size: 50 }
    end

    @filteredTweets = result['hits']['hits'] #array
    @id = SSEManager.get_id
  end

end
