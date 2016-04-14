class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :exception


  def set_amazon_es
    # require 'patron'
    require 'faraday_middleware/aws_signers_v4'
    require 'elasticsearch'


    @es_client = Elasticsearch::Client.new url: Rails.application.config.es_host do |f|
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


end