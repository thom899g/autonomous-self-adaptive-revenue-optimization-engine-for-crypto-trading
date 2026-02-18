class RiskManager:
    def __init__(self):
        self.position_size = 0
        self.max_risk = 0.05  # 5% risk per trade
        
    def calculate_risk(self, entry_price, stop_loss):
        """
        Calculates the risk for a given position.
        Args:
            entry_price (float): Entry price of the position.
            stop_loss (float): Stop loss price.
        Returns:
            float: Risk percentage.
        """
        return ((entry_price - stop_loss) / entry_price) * 100
        
    def manage_position(self, action):
        """
        Manages the position based on risk tolerance.
        Args:
            action (dict): Action taken by the strategy.
        """
        if 'entry' in action:
            risk = self.calculate_risk(action['entry'], action.get('stop_loss', 0))
            if risk > self.max_risk:
                raise ValueError("Risk exceeds maximum allowed")