module SSEManager

  @msg_stack = {} # with key(id) as str
  @id = 0
  LIMIT = 14
  # if tweets come too fast, the LIMIT has to be greater.
  # otherwise, the crowded stack will be mistaken as inactive SSE


  def self.get_id
    ## set up a new stack for SSE messages
    @id += 1 # a naive way for define unique id for each request
    @msg_stack[@id.to_s] = []
    @id
  end

  def self.publish(msg)
    @msg_stack.delete_if{ |id, stack|
      if (stack.length == LIMIT)
        ## when any stack reach this limit, the corresponding SSE(id) is
        # considered inactive, and the stack will be removed
        true
      else
        stack.push(msg)
        puts id, stack.length
        false
      end
    }
  end

  def self.get_msg(id) #id is str
    if @msg_stack.has_key?(id)
      if @msg_stack[id].length != 0
        return @msg_stack[id].pop()
      end
    else
      puts "+++++++++++++++ error +++++++++++++++++"
    end

  end



end

