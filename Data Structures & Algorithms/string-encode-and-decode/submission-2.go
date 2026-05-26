// N = # input strings in encode
// M = length of all strings max

// Encode = O ( N )
// Decode = O ( M )

// Enode + Decode = O ( N + M )

type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    out := ""
    delimeter := "@"
    for _, str := range strs { // O ( N )
        length := len(str)
        out += strconv.Itoa(length) + delimeter + str
    }
    return out
}

func (s *Solution) Decode(str string) []string {
    out := []string{}
    delimeter := byte('@')

    for i := 0; i < len(str); { // O ( M )
        length_string := ""
        j := i
        for ; j < len(str) && str[j] != delimeter ; {
            j++
        }
        if j == len(str) {
            fmt.Errorf("Decode Error: missing delimeter\n")
            return []string{}
        }
        length_string = str[i:j]
        i = j + 1
        length_int, err := strconv.Atoi(length_string)
        if err != nil {
            fmt.Errorf("Decode Error: Encoded string length is not a valid integer")
            return []string{}
        }
        word := str[i:i + length_int]
        out = append(out, word)
        i = i + length_int
    }

    return out
}
