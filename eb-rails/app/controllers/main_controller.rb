class MainController < ApplicationController

  def home
  end

  def show
    keyword = params[:keyword] || 'all'
    puts keyword

    # render text: "hello, world!"
  end

end
