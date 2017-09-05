if player:
	if player.isFlying():
		player.setAllowFlight(False)
		player.setFlying(False)
	else:
		player.setAllowFlight(True)
		player.setFlying(True)