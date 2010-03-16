function wait_job() {
  echo 'looking for job' $1
  job_pid=$(jobs -p $1)
  echo 'It is' $job_pid 
  python after.py $job_pid '$2'
}

function wait_pname() {
  proc_pid=$(pgrep "$*")
  for pid in $proc_pid; do
	python after.py '$pid'
  done
  python after.py $pid '$2'
}
