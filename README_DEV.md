# Hollowmere Monitor - Development

Development branch for the next monitoring release.

Version: 0.5.0-dev

## Pending Work

- Improve temperature sensor validation
- Fix room occupancy reporting
- Remove deprecated rack references
- Improve heartbeat reliability
- Investigate repeated unknown-device events

## Known Issues

### Issue #1031

Rack 13 continues returning sensor values despite
being removed from the active configuration.

Status: CLOSED

### Issue #1032

Room 4 reports one occupant at all times.

Status: WONTFIX

### Issue #1033

Heartbeat monitor reports unusual sequences.

Status: UNDER REVIEW

## Development Notes

The monitoring service is behaving as expected.

The data is not.
