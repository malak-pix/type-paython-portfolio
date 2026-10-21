#Check Three Access Facts
MAX_FAILED = 5
role = input("Role:")
mfa_answer = input("MFA passed (yes/no):")
failed = int(input("Failed Attempts:"))
mfa_ok = mfa_answer == "yes"
print(f" MFA_OK:{mfa_ok} ")
is_privileged = role == "admin" or role == "root"
print(f" Privileged: {is_privileged}")
can_log_in = mfa_ok and failed < MAX_FAILED
print(f" Can log in:{can_log_in} ")