type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    out := ""
    delimeter := "@"
    for _, str := range strs {
        length := len(str)
        out += strconv.Itoa(length) + delimeter + str
    }
    fmt.Printf("Got: %s\n", out)
    return out
}

func (s *Solution) Decode(str string) []string {
    out := []string{}
    delimeter := byte('@')

    for i := 0; i < len(str); {
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
        fmt.Printf("Length: %s\n", length_string)
        i = j + 1
        length_int, err := strconv.Atoi(length_string)
        if err != nil {
            fmt.Errorf("Decode Error: Encoded string length is not a valid integer")
            return []string{}
        }
        word := str[i:i + length_int]
        fmt.Printf("Word: %s\n", word)
        out = append(out, word)
        i = i + length_int
    }

    return out
}
