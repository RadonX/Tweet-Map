json.array! @tweets, '_id', '_source'
# json.array! @tweets do |tweet|
#   # next if comment.marked_as_spam_by?(current_user)
#   json.id tweet['_id']
#   json.source do
#     json.user tweet['_source']['user']
#   end
# end
