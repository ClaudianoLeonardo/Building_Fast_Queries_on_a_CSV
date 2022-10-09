class Clima:
  def __init__(self, dataset):
    with open(dataset) as f:
      self.reader = reader(f)
      self.rows = list(self.reader)
      self.header = self.rows[0]
      self.rows = self.rows[1:]
      self.id_to_row = {}
      self.sentiment_sorted = {}
      self.score = {}
      for row in self.rows:
        self.id_to_row[row[1]] = row
        self.score[int(row[9])] = row
        if row[8] == '':
          row[8] = 0.0
        else:
          row[8] = float(row[8])

        
          
  
  def get_message_from_id(self, id):
    for row in self.rows:
      if row[1] == id:
        return row
      else:
        return -1
  
  def get_message_from_id_fast(self, id):
    if id in self.id_to_row:
      return self.id_to_row[id]
    else:
      return -1

  
  def get_by_sentiment(self, sentiment_inf, sentiment_sup):
    sentiments = []
    for row in self.rows:
      if row[8] >= sentiment_inf and row[8] < sentiment_sup:
         sentiments.append(row)
    return sentiments
    



  def TwoScoreSum(self, target):
    for row1 in self.rows:
      for row2 in self.rows:
        if row1[9] + row2[9] == target:
          return [row1, row2]
        return -1

  def TwoScoreSum_fast(self, target):
    for current_number in self.score:
      y = target - current_number
      if y in self.score:
        return [self.score[y], self.score[current_number]]
    return -1